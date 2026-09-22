import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const wrapper = resolve(root, "android", process.platform === "win32" ? "gradlew.bat" : "gradlew");
const env = { ...process.env };
const knownJdk = "C:\\Program Files\\Microsoft\\jdk-21.0.12.8-hotspot";
if (process.platform === "win32" && existsSync(resolve(knownJdk, "lib/jvm.cfg"))) env.JAVA_HOME = knownJdk;
const androidSdk = "C:\\Users\\ersoz\\AppData\\Local\\Android\\Sdk";
if (process.platform === "win32" && existsSync(resolve(androidSdk, "platform-tools/adb.exe"))) {
  env.ANDROID_HOME = androidSdk;
  env.ANDROID_SDK_ROOT = androidSdk;
}
const built = spawnSync(wrapper, ["assembleDebug"], { cwd: resolve(root, "android"), stdio: "inherit", shell: process.platform === "win32", env });
if (built.error) throw built.error;
if (built.status !== 0) process.exit(built.status ?? 1);

const source = resolve(root, "android/app/build/outputs/apk/debug/app-debug.apk");
const destination = resolve(root, "..", "İngilizce-Defterim.apk");
mkdirSync(dirname(destination), { recursive: true });
copyFileSync(source, destination);
console.log(`APK hazır: ${destination}`);

import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "İngilizce Defterim — Günlük çalışma alanım",
  description: "Türkçe açıklamalar, kelime kartları, zamanlar ve cümle alıştırmalarıyla kişisel İngilizce pratiği.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="tr">
      <body className="antialiased">{children}</body>
    </html>
  );
}

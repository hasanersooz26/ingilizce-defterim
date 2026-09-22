import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "İngilizce Defterim — Günlük çalışma alanım",
  description: "Türkçe açıklamalar, kelime kartları, zamanlar ve cümle alıştırmalarıyla kişisel İngilizce pratiği.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
  manifest: "/manifest.webmanifest",
  themeColor: "#2859da",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="tr">
      <head>
        <meta name="mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="default" />
        <meta name="apple-mobile-web-app-title" content="İngilizce Defterim" />
      </head>
      <body className="antialiased">{children}</body>
    </html>
  );
}

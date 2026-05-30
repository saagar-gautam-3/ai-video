import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Reel Generator",
  description: "Generate cinematic videos from stories",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}

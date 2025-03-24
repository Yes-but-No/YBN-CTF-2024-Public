import type { Metadata } from "next";
import "./globals.css";
import Nav from "../components/UI/Nav";


export const metadata: Metadata = {
  title: "Crocodile Pay",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // const { title } = useTitle();
  return (
      <html lang="en">
        <head>
          <link rel="preconnect" href="https://fonts.googleapis.com" />
          <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
          <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Leckerli+One&display=swap" rel="stylesheet" />
          <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Leckerli+One&family=Lemon&display=swap" rel="stylesheet" />
        </head>
      <body className="pt-24">
        <Nav />
        {children}
      </body>
    </html>
  );
}

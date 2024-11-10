import "@/styles/globals.css";
import { fetchAccessToken } from "@humeai/voice";
import { VoiceProvider } from "@humeai/voice-react";

export default function App({ Component, pageProps }) {
  const apiKey = "W9yUZase0P448qboSzaPmDe4q3BU424h4lopE64HISRtvHNd";
  return (
    <VoiceProvider auth={{ type: 'apiKey', value: apiKey }}
      onMessage={(message) => console.log(message)}
    >
      <Component {...pageProps} />
    </VoiceProvider>
  );
}

import "@vidstack/react/player/styles/default/theme.css";
import "@vidstack/react/player/styles/default/layouts/video.css";
import '@vidstack/react/player/styles/plyr/theme.css';

import { MediaPlayer, MediaProvider } from "@vidstack/react";
import {
  defaultLayoutIcons,
  DefaultVideoLayout,
} from "@vidstack/react/player/layouts/default";
import { PlyrLayout, plyrLayoutIcons } from "@vidstack/react/player/layouts/plyr";

export interface VideoProps {
    layout?: "default" | "plyr";
    // playButtonPlacement?: "center" | "left";
    controlsDelay?: number | undefined;
}

export default function Video({
  layout = "default",
  controlsDelay = undefined,
}: VideoProps) {
    const thumbnails = "https://files.vidstack.io/sprite-fight/thumbnails.vtt";

    const Layout = () => {
        switch (layout) {
        case "default":
            return (
                <DefaultVideoLayout
                    thumbnails={thumbnails}
                    icons={defaultLayoutIcons}
                    playbackRates={{
                      min: 0.5,
                      max: 5,
                      step: 0.5,
                    }}
                    seekStep={15}
                />
            );
        case "plyr":
            return (
                <PlyrLayout icons={plyrLayoutIcons} />
            );
        }
    }

  return (
    <MediaPlayer
      title="Sprite Fight"
      src="https://files.vidstack.io/sprite-fight/720p.mp4"
      controlsDelay={controlsDelay}
    >
      <MediaProvider />
      <Layout />
    </MediaPlayer>
  );
}

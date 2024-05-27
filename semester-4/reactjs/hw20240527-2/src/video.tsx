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
    layout: "default" | "plyr";
}
export default function Video(props: VideoProps) {
    const thumbnails = "https://files.vidstack.io/sprite-fight/thumbnails.vtt";

    const Layout = () => {
        switch (props.layout) {
        case "default":
            return (
                <DefaultVideoLayout
                    thumbnails={thumbnails}
                    icons={defaultLayoutIcons}
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
    >
      <MediaProvider />
      <Layout />
    </MediaPlayer>
  );
}

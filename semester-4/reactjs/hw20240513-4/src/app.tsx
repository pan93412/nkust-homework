import { Button, Layout, Flex } from "antd";
import { useState } from "react";

export function App() {
  const [isBoom, setIsBoom] = useState(false);
  const types = ["default", "primary", "dashed", "link", "text"] as const;
  const shapes = ["default", "circle", "round"] as const;

  return (
    <Layout>
      <Layout.Content style={{padding: "0 48px"}}>
        {isBoom ? <h1>BOOM!</h1> : null}
        <Flex wrap gap="small">
          {types.map((type) =>
            shapes.map((shape) => (
              <Button key={`${type}-${shape}`} type={type} shape={shape} onClick={() => setIsBoom(true)}>
                {type} ({shape})
              </Button>
            ))
          )}
        </Flex>
      </Layout.Content>
    </Layout>
  );
}

import { Layout, Watermark } from "antd";

export function App() {
  return (
    <Layout>
      <Layout.Content style={{ padding: "0 48px" }}>
        <Watermark content={["C111156103", "潘奕濬"]}>
          <div style={{ padding: 24, background: "#fff", minHeight: 360, minWidth: 360 }} />
        </Watermark>
      </Layout.Content>
    </Layout>
  );
}

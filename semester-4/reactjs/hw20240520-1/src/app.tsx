import { Layout, Row, Col } from "antd";

export function App() {
  return (
    <Layout>
      <Layout.Content style={{ padding: "0 48px" }}>
        <Row>
          <Col span={24}>col</Col>
        </Row>
        <Row>
          <Col span={12}>col-12</Col>
          <Col
            span={12}
            style={{
              backgroundColor: "#FCFCFC",
            }}
          >
            col-12
          </Col>
        </Row>
        <Row>
          <Col span={8}>col-8</Col>
          <Col
            span={8}
            style={{
              backgroundColor: "#FCFCFC",
            }}
          >
            col-8
          </Col>
          <Col span={8}>col-8</Col>
        </Row>
        <Row>
          <Col span={4}>col-4</Col>
          <Col
            span={4}
            style={{
              backgroundColor: "#FCFCFC",
            }}
          >
            col-4
          </Col>
          <Col span={4}>col-4</Col>
          <Col
            span={4}
            style={{
              backgroundColor: "#FCFCFC",
            }}
          >
            col-4
          </Col>
          <Col span={4}>col-4</Col>
          <Col
            span={4}
            style={{
              backgroundColor: "#FCFCFC",
            }}
          >
            col-4
          </Col>
        </Row>
      </Layout.Content>
    </Layout>
  );
}

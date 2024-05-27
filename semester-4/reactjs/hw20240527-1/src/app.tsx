import { Breadcrumb, Layout, Menu, theme } from 'antd';
import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';

const { Header, Content, Footer } = Layout;

export function App() {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const { t, i18n } = useTranslation();
  const languages = ['en', 'ja', 'cn', 'tw'];
  const [selectedLanguage, setSelectedLanguage] = useState(i18n.language);

  useEffect(() => {
    i18n.changeLanguage(selectedLanguage);
  }, [i18n, selectedLanguage]);

  return (
    <Layout>
      <Header style={{ display: 'flex', alignItems: 'center' }}>
        <div className="demo-logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={[selectedLanguage]} items={languages.map((l) => {
          return { key: l, label: t(l) };
        })} style={{ flex: 1, minWidth: 0 }} onSelect={(info) => setSelectedLanguage(info.key)} />
      </Header>
      <Content style={{ padding: '0 48px' }}>
        <Breadcrumb style={{ margin: '16px 0' }} items={[
          {key: "home", title: t('home')},
          {key: "list", title: t('list')},
          {key: "app", title: t('app')},
        ]} />
        <div
          style={{
            background: colorBgContainer,
            minHeight: 280,
            padding: 24,
            borderRadius: borderRadiusLG,
          }}
        >
          {t('content')}
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        {t('copyright', { year: new Date().getFullYear() })}
      </Footer>
    </Layout>
  );
}

import { use as i18nUse } from "i18next";
import { initReactI18next } from "react-i18next";

import { en, ja, cn, tw } from "./locale";

i18nUse(initReactI18next).init({
  // the translations
  // (tip move them in a JSON file and import them,
  // or even better, manage them via a UI: https://react.i18next.com/guides/multiple-translation-files#manage-your-translations-with-a-management-gui)
  resources: { en, ja, cn, tw },
  fallbackLng: "en",

  interpolation: {
    escapeValue: false, // react already safes from xss => https://www.i18next.com/translation-function/interpolation#unescape
  },
});

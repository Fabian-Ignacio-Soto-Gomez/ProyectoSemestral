import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import { es, en } from "./translations"

const resources = {
    en: {
        translation: en,
    },
    es: {
        translation: es,
    },
}

i18n.use(initReactI18next).init({
    debug: true,
    lng: "es",
    fallbackLng : 'es',
    interpolation: {
        escapeValue: false,
    },
    resources,

})

export default i18n;
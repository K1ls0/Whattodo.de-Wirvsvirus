import i18n from 'i18next';
import {reactI18nextModule} from 'react-i18next';
import languageEN from "web/src/lang/langEN.json"
import languageDE from "web/src/lang/langDE.json"

const resources = {
    en: {
        translation: languageEN
    },
    de: {
        translation: languageDE
    }
};

i18n.use(reactI18nextModule) // passes i18n down to react-i18next
    .init({
        resources,
        lng: "de",

        keySeparator: false, // we do not use keys in form messages.welcome

        interpolation: {
            escapeValue: false // react already safes from xss
        }
    }).then(() => {});

export default i18n;
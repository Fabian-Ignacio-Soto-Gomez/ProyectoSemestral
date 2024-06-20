import { useTranslation } from "react-i18next";
import { Link } from "react-router-dom";

export function Navbar() {
  const { t, i18n } = useTranslation();

  return (
    <nav className="bg-gray-800 p-4">
      <div className="flex flex-wrap items-center justify-between">
        <div className="flex items-center flex-shrink-0 text-white mr-6">
          <img src="src/img/Logo_Universidad_Adolfo_Ibáñez.JPG" alt="Logo" className="h-12 w-auto mr-2 m-0" />
        </div>
        <div className="block lg:hidden">
          <button className="flex items-center px-3 py-2 border rounded text-gray-200 border-gray-400 hover:text-white hover:border-white" onClick={() => console.log("Menu button clicked")}>
            <svg className="h-3 w-3 fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
          </button>
        </div>
        <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
          <div className="text-sm lg:flex-grow">
            <Link to="/" className="block mt-4 lg:inline-block lg:mt-0 text-white mr-4 hover:text-slate-300">
              {t('Navbar.link2Login')}
            </Link>
            <Link to="/c" className="block mt-4 lg:inline-block lg:mt-0 text-white mr-4 hover:text-slate-300">
              {t('Navbar.link2CreateAccount')}
            </Link>
          </div>
          <div className="mr-5">
            <button className="text-white mr-3 hover:text-slate-300" onClick={e => {
              e.preventDefault()
              i18n.changeLanguage('es')
            }}>{t('Navbar.language1')}</button>
            <button className="text-white hover:text-slate-300" onClick={e => {
              e.preventDefault()
              i18n.changeLanguage('en')
            }}>{t('Navbar.language2')}</button>
          </div>
        </div>
      </div>
    </nav>
  );
}

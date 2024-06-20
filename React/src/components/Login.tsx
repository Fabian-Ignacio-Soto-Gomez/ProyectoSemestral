import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import { getSHA256Hash } from "boring-webcrypto-sha256";
import { useTranslation } from "react-i18next";
import axios from 'axios'



export function LoginForm() {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const [emailInput, setEmailInput] = useState("");
  const [passwordInput, setPasswordInput] = useState("")




  async function handleLoginForm() {
    // Password encrypted in sha256
    const hashPasword = await getSHA256Hash(passwordInput);

    //Llamada a la API para verificar el usuario
    const data = {
      "email": emailInput,
      "password": passwordInput
    }
    const url = 'http://127.0.0.1:8000/api/login/'

    //Llamada a la API para verificar el usuario
    axios.post(url, data).then( (response) => {
      //Si el usuario existe se navega a home
      if(response.data.response){
        navigate("/home", {state:{emailState:emailInput, rolState:response.data.rol}})
      }
      else{
        alert('Email o contraseña incorrectas')
      }
    }).catch( (error) => {
      console.log(error)
    })    
    
  }

  return (
    <div className="my-10 shadow-lg max-w-sm mx-auto bg-slate-50 p-4 rounded-lg">
      <form className="space-y-6" onSubmit={(e) => e.preventDefault()}>
        <div>
          <p className="text-2xl text-center">{t("Login.title")}</p>
        </div>
        <div>
          <label htmlFor="UserEmail">{t("Login.email")}</label>
          <input
            type="email"
            id="UserEmail"
            className="w-full p-2 mb-4 rounded border border-slate-200"
            placeholder={t("Login.email")}
            onChange={(e) => setEmailInput(e.target.value)}
            value={emailInput}
            required
          />
        </div>
        <div>
          <label htmlFor="UserPassword">{t("Login.password")}</label>
          <input
            type="password"
            id="UserPassword"
            className="w-full p-2 mb-4 rounded border border-slate-200"
            placeholder={t("Login.password")}
            onChange={(e) => setPasswordInput(e.target.value)}
            value={passwordInput}
            required
          />
        </div>
        <div className="flex justify-center space-x-4">
          <button
            type="submit"
            className="rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500"
            onClick={handleLoginForm}
          >
            {t("Login.btn-form")}
          </button>

          <Link
            to="/dashboard-profesores"
            className="rounded-md bg-blue-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-500"
          >
            Ir a Dashboard de Profesores
          </Link>
        </div>
      </form>
      <div className="text-center mt-5">
        <p className="mb-2">{t("Login.span")}</p>
        <Link
          to={"/c"}
          className="text-slate-500 hover:text-slate-700"
        >
          {t("Login.link2CreateAccount")}
        </Link>
      </div>
    </div>
  );
}

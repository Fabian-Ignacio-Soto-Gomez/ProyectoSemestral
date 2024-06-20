import { useEffect, useState } from "react"
import { UploadFileForm } from "../components/UploadFIle"
import { useTranslation } from "react-i18next"
import { useLocation, useNavigate } from "react-router-dom"
import { DashboardAlumno } from "./DashboardAlumno"
import { DashboardProfesor } from "./DashboardProfesores"


export function Home(){
    

  const navigate = useNavigate()
  const { t } = useTranslation()

  const {state} = useLocation()   
  const { emailState, rolState } = state

  let page
  if (rolState == 'est'){
    page = <DashboardAlumno  />
  }
  else if(rolState == 'prof'){
    page = <DashboardProfesor />
  }

  return (
    <div>
      {/* <p>{t('Home.title')}</p>
      <p>{t('Home.text')}</p> */}
      {/* <button className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" type="submit" onClick={submitLogout}>Logout</button>
      <UploadFileForm /> */}
      {page}
      
   </div>
  )
}

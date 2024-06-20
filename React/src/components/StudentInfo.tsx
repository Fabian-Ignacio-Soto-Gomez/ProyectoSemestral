import axios from "axios"
import { useEffect, useState } from "react"

export function StudentInfo({ rut, nota, comentario, num }:{ rut:string, nota:number, comentario:string, num:number}){
  const [isChecked, SetisChecked] = useState(false)

  function handleStudentinfo(rut:string, number:number){
    const data = {
      "rut": rut
    }

    axios.post('http://127.0.0.1:8000/api/infostudent/', data).then(
      (response) => {
        const data = []
        data.push(response.data.avance_1, response.data.avance_2, response.data.avance_3)
        console.log(rut + " " + data[number])
        SetisChecked(data[number])
        // return data[number]
      }
    ).catch (( error ) => {
      console.log(error)
    })
  }

  function handleChangeAvance(rut:string, num:number){
    const data = {
      "rut": rut,
      "num": (num+1).toString(),
      "avance": !isChecked
    }

    axios.post('http://127.0.0.1:8000/api/avance/', data).then(
      (response) => {
        if (response.data.response){
          alert('Cambio realizado')
        }
        else{
          alert('Error')
        }
      }
    )
    return
  }

  useEffect(() => {
    handleStudentinfo(rut, num)
  }, [rut, num])
  
    return (
        <div className="flex flex-col">
            <div className="flex flex-  row">
                <p className="m-2">{rut}</p>
                <p className="m-2">{nota}</p>
                <p className="m-2">{comentario}</p>
                <input type="checkbox" checked={isChecked} onClick={() => handleChangeAvance(rut, num)} onChange={(e) => SetisChecked(e.target.checked)}/>
            </div>
        </div>
    )
}
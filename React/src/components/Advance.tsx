export function Advance({ avance, nota, comentario }:{ avance:boolean, nota:number, comentario:string }){

    return (
        <div className="flex flex-row">
            <div className="m-2">
                <label>
                    <input type="checkbox" checked={avance}/>
                    <span></span>
                </label>
            </div>
            <div className="m-2"><input type="file" /></div> 
            <div className="m-2"><input type="file" /></div>
            <div className="m-2">{nota}</div>
            <div className="m-2">{comentario}</div>
        </div>
    )
}
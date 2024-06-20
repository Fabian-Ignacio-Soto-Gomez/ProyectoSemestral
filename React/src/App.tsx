import { Route, Routes } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { Home } from './Pages/Home';
import { Login } from './Pages/Login';
import { CreateAccount } from './Pages/CreateAccount';
import Inscripcion from './Pages/Inscripcion';
import Revision from './Pages/Revision';

export function App() {
  return (
    <div className='bg-cover justify-center items-center h-lvh'>
      {/* Navbar */}
      <Navbar />
      
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/c" element={<CreateAccount />} />
        <Route path="/home" element={<Home />} /> 
        <Route path="/inscripcion" element={<Inscripcion />} />
        <Route path="/revision-formulario" element={<Revision />} />
      </Routes>
    </div>
  );
}

export default App;

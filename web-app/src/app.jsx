import { BrowserRouter, Routes, Route } from 'react-router-dom';
import RegisterPage from './pages/register';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="register" element={<RegisterPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
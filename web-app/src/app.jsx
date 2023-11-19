import { BrowserRouter, Routes, Route } from 'react-router-dom';
import RegisterPage from './pages/register';
import AddRequestPage from './pages/add_request';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="register" element={<RegisterPage />} />
        <Route path='request-add' element={<AddRequestPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
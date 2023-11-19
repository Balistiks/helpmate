import { useState } from "react";
import Input from "../../widgets/input"
import './index.css'

const RegisterPage = () => {
  const [name, setName] = useState('')
  const [phoneNumber, setPhoneNumber] = useState('')
  const [adress, setAdress] = useState('')

  return(
    <div className="register-container">
      <h2>Форма Регистрации</h2>
      <div className="form-group">
        <label htmlFor="name">Введите ФИО:</label>
        <Input value={name} onChange={(value) => setName(value)} />
      </div>

      <div className="form-group">
        <label htmlFor="phoneNumber">Введите номер телефона:</label>
        <Input value={phoneNumber} onChange={(value) => setPhoneNumber(value)} />
      </div>

      <div className="button-holder">
        <button >Подтвердить</button>
      </div>
    </div>
  );
}

export default RegisterPage;
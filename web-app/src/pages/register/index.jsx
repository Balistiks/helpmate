import { useState } from "react";
import Input from "../../widgets/input"
import './index.css'

const RegisterPage = () => {
  const [name, setName] = useState('')
  const [phoneNumber, setPhoneNumber] = useState('')
  const [adress, setAdress] = useState('')
  const onChangeNameHandler = (value) => {
    setName(value)
  }

  return(
    <>
      <p>Введите ФИО:</p>
      <Input value={name} onChange={(value) => setName(value)} />
      <p>Введите номер телефона:</p>
      <Input value={phoneNumber} onChange={(value) => setPhoneNumber(value)} />
      <p>Введите свой адрес:</p>
      <Input value={adress} onChange={(value) => setAdress(value)} />
      <div className="button-holder">
        <button>Подвердить</button>
      </div>
    </>
  );
}

export default RegisterPage;
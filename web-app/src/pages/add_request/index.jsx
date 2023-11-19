import { useState } from "react"
import Input from "../../widgets/input";
import "./index.css"

const AddRequestPage = () => {
  const [description, setDescription] = useState('');
  const [adress, setAdress] = useState('');
  const [category, setCategory] = useState('');
  const [data, setData] = useState('');
  const [time, setTime] = useState('');

  return (
    <>
      <p>Напишите описание услуги:</p>
      <Input value={description} onChange={(value) => setDescription(value)} />
      <p>Напишите описание услуги:</p>
      <Input value={adress} onChange={(value) => setAdress(value)} />
      <p>Выберите категорию</p>
      <div>
        <select value={category} onChange={(event) => setCategory(event.target.value)}>
          <option value='сантехника'>сантехника</option>
          <option value='репетитор'>репетитор</option>
          <option value='инструктор по вождению'>инструктор по вождению</option>
          <option value='клининг'>клининг</option>
        </select>
      </div>
      <p>Напишите желаемую дату:</p>
      <Input value={data} onChange={(value) => setData(value)} />
      <p>Напишите желаемое время:</p>
      <Input value={time} onChange={(value) => setTime(value)} />
    </>
  );
}

export default AddRequestPage;
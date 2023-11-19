import { useState } from "react"
import Input from "../../widgets/input";
import "./index.css"

const AddRequestPage = () => {
  const [description, setDescription] = useState('');
  const [adress, setAdress] = useState('');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');

  return (
    <div className="add-request-container">
      <h2>Добавить Запрос</h2>
      <div className="form-group">
        <label htmlFor="description">Напишите описание услуги:</label>
        <Input value={description} onChange={(value) => setDescription(value)} />
      </div>

      <div className="form-group">
        <label htmlFor="address">Напишите адрес:</label>
        <Input value={adress} onChange={(value) => setAdress(value)} />
      </div>

      <div className="form-group">
        <label htmlFor="category">Выберите категорию:</label>
        <select
          value={category}
          onChange={(event) => setCategory(event.target.value)}
        >
          <option value="сантехника">Сантехника</option>
          <option value="репетитор">Репетитор</option>
          <option value="инструктор по вождению">Инструктор по вождению</option>
          <option value="клининг">Клининг</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="date">Напишите желаемую дату:</label>
        <Input value={date} onChange={(value) => setDate(value)} />
      </div>

      <div className="form-group">
        <label htmlFor="time">Напишите желаемое время:</label>
        <Input value={time} onChange={(value) => setTime(value)} />
      </div>
    </div>
  );
}

export default AddRequestPage;
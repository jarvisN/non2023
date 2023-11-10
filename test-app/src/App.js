import logo from './logo.svg';
import './App.css';
import myImage from './images/non.jpg'; // เปลี่ยนเส้นทางไปยังไฟล์รูปภาพของคุณ


function SendDataButton() {
  // ข้อมูลที่จะส่งไปยังเซิร์ฟเวอร์
  const dataToSend = {
    key1: 'value1',
    key2: 'value2'
  };

  // ฟังก์ชันสำหรับส่งข้อมูล
  const sendDataToServer = () => {
    fetch('https://your-server.com/api/endpoint', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSend),
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Something went wrong on api server!');
      })
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <button onClick={sendDataToServer}>
      ส่งข้อมูล
    </button>
  );
}




function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" width="200" height="150" />
        <p>
          <img src={myImage} alt="รายละเอียดรูปภาพ" width="200" height="150" />
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>
          <SendDataButton />
        </p>
      </header>
    </div>
  );
}

export default App;

import { useEffect } from "react";

function App() {
  useEffect(() => {
    fetch("/home")
        .then((r) => r.json())
        .then((data) => console.log(data))
  }
  ,[])

  return (
    <div>Thing</div>
  );
}

export default App;

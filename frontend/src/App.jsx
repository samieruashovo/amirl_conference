import logo from "./logo.svg";
import Layout from "./components/Layout";
import HomePage from "./components/HomePage";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div className="App">
      <Layout>
        <HomePage />
        <div className="app container mt-3 mb-3 text-dark"></div>
        {/* <HomePage /> */}
      </Layout>
    </div>
  );
}

export default App;

import logo from "./logo.svg";
import Layout from "./components/Layout";
import HomePage from "./components/HomePage";
import "bootstrap/dist/css/bootstrap.min.css";

function App({ conferences }) {
  console.log(conferences);
  return (
    <div className="App">
      <Layout>
        <HomePage conferences={conferences} />
        <div className="app container mt-3 mb-3 text-dark"></div>
        {/* <HomePage /> */}
      </Layout>
    </div>
  );
}

export default App;

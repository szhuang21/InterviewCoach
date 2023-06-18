import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./pages/Home";

/**
 * provides routing to different pages
 */
function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;

// import "./App.css";
// import Video from "./components/Video";

// function App() {
//   return (
//     <div className="App">
//       {/* <Video/> */}
//     </div>
//   );
// }

// export default App;

import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./pages/Home";
import Report from "./pages/Report";
import Video from "./components/Video";
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
        <Route exact path="/Video">
          <Video />
        </Route>
        <Route exact path="/Report">
          <Report />
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

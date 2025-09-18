import React from "react";
import './App.css'
import {
  BrowserRouter as Router,
  Routes as Switch,
  Route,
  useHistory  
} from "react-router-dom";

import ImageInput from "./views/imageInput";
import Recommendations from './views/Recommendations'

// MUI
import CssBaseline from '@mui/material/CssBaseline';

function App() {
  return (
    <>
      <CssBaseline />
      <Router>
      
        <Switch>
          <Route path="/" element={<ImageInput />} />

          <Route path="/recs" element={<Recommendations />} />
        </Switch>

      </Router>
    </>

  );
}

export default App;

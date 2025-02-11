import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import InvestorsList from "./components/InvestorsList";
import InvestorDetails from "./components/InvestorDetails";
import { CssBaseline, Container } from "@mui/material";

/**
 * App Component
 *
 * This is the main entry point of the application. It sets up the React Router
 * to navigate between the list of investors and individual investor details.
 * It also applies global styles using Material UI's CssBaseline.
 */
function App() {
  return (
    <Router>
      {/* Ensures consistent baseline styles across different browsers */}
      <CssBaseline />
      <Container>
        <Routes>
          {/* Route for displaying the list of investors */}
          <Route path="/" element={<InvestorsList />} />
          {/* Route for displaying details of a specific investor */}
          <Route path="/investor/:id" element={<InvestorDetails />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;

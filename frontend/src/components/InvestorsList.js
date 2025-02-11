import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useParams,
  Link,
} from "react-router-dom";
import {
  CssBaseline,
  Container,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Chip,
  Box,
} from "@mui/material";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

// Registering ChartJS components
ChartJS.register(Title, Tooltip, Legend);

const API_BASE_URL = "http://localhost:8000";

/**
 * InvestorsList Component
 *
 * This component fetches and displays a list of investors along with their total commitments.
 * It also provides a visual representation of the total commitments using a bar chart.
 */
function InvestorsList() {
  const [investors, setInvestors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch investor data on component mount
  useEffect(() => {
    fetch(`${API_BASE_URL}/investors_with_totals`)
      .then((response) => response.json())
      .then((data) => {
        setInvestors(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching investors:", err);
        setError(err.message);
        setLoading(false);
      });
  }, []);

  // Prepare data for the bar chart
  const chartData = {
    labels: investors.map((investor) => investor.name),
    datasets: [
      {
        label: "Total Commitments (GBP)",
        data: investors.map((investor) => investor.total_commitments_gbp),
        backgroundColor: "rgba(75, 192, 192, 0.6)",
      },
    ],
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Investors
      </Typography>
      {loading && <p>Loading investors...</p>}
      {error && <p style={{ color: "red" }}>Error: {error}</p>}

      {!loading && !error && (
        <>
          {/* Table displaying investor details */}
          <TableContainer component={Paper}>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>ID</TableCell>
                  <TableCell>Name</TableCell>
                  <TableCell>Type</TableCell>
                  <TableCell>Country</TableCell>
                  <TableCell>Date Added</TableCell>
                  <TableCell>Total Commitments</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {investors.map((investor) => (
                  <TableRow key={investor.id}>
                    <TableCell>{investor.id}</TableCell>
                    <TableCell>
                      <Link to={`/investor/${investor.id}`}>
                        {investor.name}
                      </Link>
                    </TableCell>
                    <TableCell>{investor.investor_type}</TableCell>
                    <TableCell>{investor.country}</TableCell>
                    <TableCell>{investor.date_added}</TableCell>
                    <TableCell>
                      <Chip
                        label={
                          investor.total_commitments_gbp >= 1e9
                            ? `£${(
                                investor.total_commitments_gbp / 1e9
                              ).toFixed(1)}B`
                            : `£${(
                                investor.total_commitments_gbp / 1e6
                              ).toFixed(1)}M`
                        }
                        color="primary"
                      />
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>

          {/* Bar chart visualizing total commitments */}
          <Box mt={4}>
            <Typography variant="h5" align="center" gutterBottom>
              Total Commitments Breakdown
            </Typography>
            <Bar data={chartData} />
          </Box>
        </>
      )}
    </Container>
  );
}

export default InvestorsList;

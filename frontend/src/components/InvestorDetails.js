import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import {
  Container,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Button,
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
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const API_BASE_URL = "http://localhost:8000";

/**
 * InvestorDetails Component
 *
 * This component fetches and displays detailed information about a selected investor.
 * It includes a breakdown of commitments and allows filtering by asset class.
 */
function InvestorDetails() {
  const { id } = useParams(); // Extract investor ID from URL params
  const [investor, setInvestor] = useState(null);
  const [assetClassFilter, setAssetClassFilter] = useState("");

  // Fetch investor details on component mount
  useEffect(() => {
    fetch(`${API_BASE_URL}/investors/${id}`)
      .then((response) => response.json())
      .then((data) => setInvestor(data))
      .catch((error) =>
        console.error("Error fetching investor details:", error)
      );
  }, [id]);

  if (!investor) return <p>Loading investor details...</p>;

  // Filter commitments based on selected asset class
  const filteredCommitments = assetClassFilter
    ? investor.commitments.filter((c) => c.asset_class === assetClassFilter)
    : investor.commitments;

  // Calculate total commitments for selected asset class or all
  const totalCommitment = filteredCommitments.reduce(
    (sum, c) => sum + c.amount,
    0
  );

  return (
    <Container>
      {/* Page header with investor name and navigation button */}
      <Box
        display="flex"
        justifyContent="space-between"
        alignItems="center"
        mb={2}
      >
        <Typography variant="h4">{investor.name} - Commitments</Typography>
        <Button variant="contained" color="primary" component={Link} to="/">
          Back to Investors List
        </Button>
      </Box>

      {/* Display total commitments */}
      <Typography variant="h6" color="primary" gutterBottom>
        Total Commitments for {assetClassFilter || "All"}: £
        {(totalCommitment / 1e6).toFixed(1)}M
      </Typography>

      {/* Dropdown filter for asset class selection */}
      <FormControl fullWidth style={{ marginTop: "20px" }}>
        <InputLabel>Filter by Asset Class</InputLabel>
        <Select
          value={assetClassFilter}
          onChange={(e) => setAssetClassFilter(e.target.value)}
        >
          <MenuItem value="">All</MenuItem>
          {[...new Set(investor.commitments.map((c) => c.asset_class))].map(
            (assetClass) => (
              <MenuItem key={assetClass} value={assetClass}>
                {assetClass}
              </MenuItem>
            )
          )}
        </Select>
      </FormControl>

      {/* Table displaying commitment details */}
      <TableContainer component={Paper} style={{ marginTop: "20px" }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Asset Class</TableCell>
              <TableCell>Currency</TableCell>
              <TableCell>Amount (GBP)</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredCommitments.map((commitment) => (
              <TableRow key={commitment.id}>
                <TableCell>{commitment.id}</TableCell>
                <TableCell>{commitment.asset_class}</TableCell>
                <TableCell>{commitment.currency}</TableCell>
                <TableCell>£{(commitment.amount / 1e6).toFixed(1)}M</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
}

export default InvestorDetails;

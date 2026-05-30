import apiClient from './api';

export async function fetchHealth() {
  try {
    const response = await apiClient.get('/health');
    return response.data;
  } catch (error) {
    throw new Error('Failed to fetch health status');
  }
}

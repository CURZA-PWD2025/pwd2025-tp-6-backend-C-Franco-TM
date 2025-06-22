import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:5000",
  headers: {
    "Content-Type": "application/json",
  },
});

export default {
  getAll(resource: string) {
    return apiClient.get(`/${resource}/`);
  },
  getOne(resource: string, id: number) {
    return apiClient.get(`/${resource}/${id}`);
  },
  create(resource: string, data: any) {
    return apiClient.post(`/${resource}/`, data);
  },
  update(resource: string, id: number, data: any) {
    return apiClient.put(`/${resource}/${id}`, data);
  },
  delete(resource: string, id: number) {
    return apiClient.delete(`/${resource}/${id}`);
  },
};

import ApiService from "./ApiService";

const endpoint = "/categorias/";

export default {
  async getAll() {
    const response = await ApiService.get(endpoint);
    return response.data;
  }
};

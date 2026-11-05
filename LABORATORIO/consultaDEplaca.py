// plate.js
import { createVehiclesApi } from 'apigratis-sdk-nodejs';

// 5.1 – Instância da API
const vehiclesApi = createVehiclesApi({
  BearerToken: process.env.BEARER_TOKEN,
  DeviceToken: process.env.DEVICE_TOKEN,
});

// 5.2 – Função principal
async function consultarPlaca(placa) {
  try {
    const resp = await vehiclesApi.request('/dados', { placa });
    console.log(JSON.stringify(resp, null, 2));
  } catch (err) {
    console.error('Erro ao consultar placa:', err.message);
  }
}

// 5.3 – Execução
consultarPlaca('ABC1D23');
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Diff',         # aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acum_anterior = 0.0  # acumulador anterior

    def work(self, input_items, output_items):
        x = input_items[0]   # Señal de entrada
        y0 = output_items[0] # Señal acumulada diferencial

        # número de muestras en este bloque
        N = len(x)

        # suma acumulativa con offset del bloque anterior
        diff = np.cumsum(x) + self.acum_anterior

        # guardar último valor para el siguiente bloque
        self.acum_anterior = diff[-1]

        # salida
        y0[:] = diff
        return len(y0)

from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.media

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.label_output.text = "(Unggah gambar untuk klasifikasi)"
    self.label_output.text_color = "black"
    self.image_1.source = None

  def file_loader_1_change(self, file, **event_args):
    """
    Saat user upload gambar manual.
    """
    if file:
      self.image_1.source = file
      self.label_output.text = "(Gambar siap diklasifikasi)"
      self.label_output.text_color = "black"

  def button_submit_click(self, **event_args):
    """
    Proses klasifikasi setelah tombol diklik.
    """
    file = self.file_loader_1.file

    if file:
      # Tampilkan gambar di preview
      self.image_1.source = file

      # Kirim ke server dan dapatkan hasil
      hasil = anvil.server.call('klasifikasi_nanas', file)

      # Tampilkan hasil prediksi
      self.label_output.text = f"Hasil Klasifikasi: {hasil}"
    else:
      self.label_output.text = "Silakan unggah gambar terlebih dahulu."
import anvil.server
import anvil.media

@anvil.server.callable
def klasifikasi_nanas(file):
  """
  Menerima file gambar dari Form1, mengubahnya menjadi bytes,
  dan meneruskan ke fungsi klasifikasi yang berjalan di Colab via Uplink.
  """
  if not file:
    return "Error: Tidak ada gambar yang diberikan."

  try:
    # Ambil data bytes dari file media
    image_bytes = file.get_bytes()
    print("Mengirim gambar ke Colab untuk klasifikasi...")

    # Panggil fungsi klasifikasi yang ada di Google Colab via Uplink
    hasil = anvil.server.call('klasifikasi_nanas', image_bytes)

    return hasil

  except Exception as e:
    return f"Error saat klasifikasi: {str(e)}"
import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_memory_growth(gpus[0], True)
        tf.config.set_visible_devices(gpus[0], 'GPU')
        print("✅ GPU configurada com crescimento dinâmico")
    except RuntimeError as e:
        print("⚠️ Erro ao configurar GPU:", e)
else:
    print("⚠️ Nenhuma GPU detectada. Usando CPU.")

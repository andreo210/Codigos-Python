import tensorflow as tf


def configurar_gpu_segura(modo='growth', memoria_limite_mb=1024):
    """
    Configura a GPU com segurança:
    - modo='growth' → crescimento dinâmico
    - modo='limit' → limite fixo de memória
    """
    gpus = tf.config.list_physical_devices('GPU')
    if not gpus:
        print("⚠️ Nenhuma GPU detectada. Usando CPU.")
        return

    try:
        if modo == 'limit':
            tf.config.experimental.set_virtual_device_configuration(
                gpus[0],
                [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=memoria_limite_mb)]
            )
            print(f"✅ GPU configurada com limite de {memoria_limite_mb} MB")
        elif modo == 'growth':
            tf.config.experimental.set_memory_growth(gpus[0], True)
            print("✅ GPU configurada com crescimento dinâmico")
        else:
            print(f"⚠️ Modo inválido: '{modo}'. Use 'growth' ou 'limit'.")
    except RuntimeError as e:
        print(f"⚠️ Erro ao configurar GPU: {e}")

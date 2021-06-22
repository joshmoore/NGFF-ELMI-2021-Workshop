def setup_minio():
  return {
      # 'command': ['nohup', 'minio', '--address', ':{port}', 'server', '/home/joyvan', '&']
      'command': ['bash', 'minio.sh', ':{port}'],
      'timeout': 10,
      'absolute_url': False, # True works locally
  }

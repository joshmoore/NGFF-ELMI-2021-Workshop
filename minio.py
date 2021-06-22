def setup_minio():
  return {
      'command': ['minio', '--address', ':{port}', 'server', '/home/joyvan']
  }

import setuptools

setuptools.setup(
  name="jupyter-minio-server",
  py_modules=['minio'],
  entry_points={
      'jupyter_serverproxy_servers': [
          'minio = minio:setup_minio',
      ]
  },
  install_requires=['jupyter-server-proxy'],
)

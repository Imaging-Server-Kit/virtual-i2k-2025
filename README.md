![EPFL Center for Imaging logo](https://imaging.epfl.ch/resources/logo-for-gitlab.svg)
# 🪐 Enrich your Python Workflow with the Imaging Server Kit

Material for the [2025 Virtual Halfway to I2K](https://www.i2kconference.org/) *Imaging Server Kit* workshop.

- [introduction.ipynb](./introduction.ipynb) - Boilerplate notebook to create server kit algorithms.
- [server.py](./server.py) - Boilerplate script for serving algorithms.

## Useful links

[**🏠 Project Homepage**](https://github.com/Imaging-Server-Kit)

[**📔 Documentation**](https://imaging-server-kit.github.io/imaging-server-kit/)

[**💡 Idea Box**](https://forms.gle/XDi5YKc71LTBWUzY9) - Let us know about your experience with the Imaging Server Kit!

[**✏️ Issues**](https://github.com/Imaging-Server-Kit/imaging-server-kit/issues) - If you encounter any issues while using the server kit, please file them in the repository. Thank you!

## Setup

If you haven't done so already, you can install the Imaging Server Kit package via `pip`:

```
pip install imaging-server-kit
```

To use Napari-related functionalities, you will also need to install the **Napari plugin**:

```
pip install "napari[all]" napari-serverkit
```

To use algorithms in QuPath, install the extension from [this page](https://github.com/Imaging-Server-Kit/qupath-extension-serverkit/releases) (choose the latest release).
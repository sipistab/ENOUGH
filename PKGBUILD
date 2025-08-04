# Maintainer: Sipos Istvan <sipistab@gmail.com>
pkgname=enough-journal
pkgver=0.2.0
pkgrel=1
pkgdesc="A minimal journaling application with Nathaniel Branden sentence completion exercises"
arch=('any')
url="https://github.com/sipistab/enough"
license=('CC0')
depends=('python' 'python-pyyaml')
makedepends=('python-build' 'python-installer' 'python-wheel')
source=("$pkgname-$pkgver.tar.gz::https://github.com/sipistab/enough/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
  cd "enough-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "enough-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
} 
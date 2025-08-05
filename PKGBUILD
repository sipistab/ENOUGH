# Maintainer: DAX <dax@example.com>
pkgname=enough-journal
pkgver=0.3.1
pkgrel=1
pkgdesc="Nathaniel Branden Sentence Completion Journal"
arch=('any')
url="https://github.com/sipistab/ENOUGH"
license=('CC0')
depends=('python' 'python-pyyaml')
makedepends=('python-setuptools' 'python-wheel' 'python-build')
source=("https://github.com/sipistab/ENOUGH/archive/refs/tags/v0.3.1.tar.gz")
sha256sums=("SKIP")

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
} 
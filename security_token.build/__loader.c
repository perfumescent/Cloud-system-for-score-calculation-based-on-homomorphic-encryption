
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

#include "nuitka/constants_blob.h"

#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 0 > 0
static unsigned char *bytecode_data[0];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode___main__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$ber(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$ber$decoder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$ber$encoder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$ber$eoo(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$cer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$cer$decoder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$cer$encoder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$der(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$der$decoder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$codec$der$encoder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$compat$binary(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$compat$calling(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$compat$dateandtime(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$compat$integer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$compat$octets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$compat$string(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$debug(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$error(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$char(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$constraint(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$error(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$namedtype(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$namedval(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$tag(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$tagmap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$univ(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyasn1$type$useful(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$asn1(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$key(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$parallel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$pem(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$pkcs1(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$prime(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$randnum(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_rsa$transform(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"__main__", modulecode___main__, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1", modulecode_pyasn1, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pyasn1.codec", modulecode_pyasn1$codec, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pyasn1.codec.ber", modulecode_pyasn1$codec$ber, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pyasn1.codec.ber.decoder", modulecode_pyasn1$codec$ber$decoder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.codec.ber.encoder", modulecode_pyasn1$codec$ber$encoder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.codec.ber.eoo", modulecode_pyasn1$codec$ber$eoo, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.codec.cer", modulecode_pyasn1$codec$cer, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pyasn1.codec.cer.decoder", modulecode_pyasn1$codec$cer$decoder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.codec.cer.encoder", modulecode_pyasn1$codec$cer$encoder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.codec.der", modulecode_pyasn1$codec$der, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pyasn1.codec.der.decoder", modulecode_pyasn1$codec$der$decoder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.codec.der.encoder", modulecode_pyasn1$codec$der$encoder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.compat", modulecode_pyasn1$compat, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pyasn1.compat.binary", modulecode_pyasn1$compat$binary, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.compat.calling", modulecode_pyasn1$compat$calling, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.compat.dateandtime", modulecode_pyasn1$compat$dateandtime, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.compat.integer", modulecode_pyasn1$compat$integer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.compat.octets", modulecode_pyasn1$compat$octets, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.compat.string", modulecode_pyasn1$compat$string, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.debug", modulecode_pyasn1$debug, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.error", modulecode_pyasn1$error, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type", modulecode_pyasn1$type, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pyasn1.type.base", modulecode_pyasn1$type$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.char", modulecode_pyasn1$type$char, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.constraint", modulecode_pyasn1$type$constraint, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.error", modulecode_pyasn1$type$error, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.namedtype", modulecode_pyasn1$type$namedtype, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.namedval", modulecode_pyasn1$type$namedval, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.tag", modulecode_pyasn1$type$tag, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.tagmap", modulecode_pyasn1$type$tagmap, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.univ", modulecode_pyasn1$type$univ, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyasn1.type.useful", modulecode_pyasn1$type$useful, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa", modulecode_rsa, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"rsa.asn1", modulecode_rsa$asn1, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.common", modulecode_rsa$common, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.core", modulecode_rsa$core, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.key", modulecode_rsa$key, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.parallel", modulecode_rsa$parallel, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.pem", modulecode_rsa$pem, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.pkcs1", modulecode_rsa$pkcs1, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.prime", modulecode_rsa$prime, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.randnum", modulecode_rsa$randnum, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"rsa.transform", modulecode_rsa$transform, 0, 0, NUITKA_TRANSLATED_FLAG},
    {NULL, NULL, 0, 0, 0}
};

static void _loadBytesCodesBlob()
{
    static bool init_done = false;

    if (init_done == false) {
        loadConstantsBlob((PyObject **)bytecode_data, ".bytecode");

        init_done = true;
    }
}


void setupMetaPathBasedLoader(void) {
    static bool init_done = false;
    if (init_done == false) {
        _loadBytesCodesBlob();
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }


}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {

    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    _loadBytesCodesBlob();

    struct frozen_desc *current = _frozen_modules;

    for (;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;

        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}



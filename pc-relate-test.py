import numpy as np
import sgkit as sg
from sgkit.stats.aggregation import allele_frequency
import xarray as xr
import dask.array as da

ds = sg.load_dataset("output2.zarr")
ds = xr.Dataset(data_vars=dict(
        call_genotype=(("variants", "samples", "ploidy"), ds['call_genotype']),
        call_genotype_mask=(("variants", "samples", "ploidy"), ds['call_genotype_mask']),
        call_genotype_phased=(("variants", "samples"), ds['call_genotype_phased']),
        sample_id=(("samples"), ds['sample_id']),
        variant_allele=(("variants","alleles"), ds['variant_allele'][:,0:2]),
        variant_contig=(("variants"), ds['variant_contig']),
        variant_id=(('variants'), ds['variant_id']),
        variant_id_mask=(('variants'), ds['variant_id_mask']),
        variant_position=(('variants'), ds['variant_position'])
    ))

rel = sg.pca(ds)

pc_relate_result = sg.pc_relate(rel, sample_pcs='sample_pca_component')
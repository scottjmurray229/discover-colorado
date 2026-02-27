// Shared destination coordinates — single source of truth
// Used by plan page + companion app + generate-itinerary API.

export const DESTINATION_COORDS: Record<string, { lat: number; lng: number; label: string }> = {
  denver: { lat: 39.7392, lng: -104.9903, label: 'Denver' },
  boulder: { lat: 40.0150, lng: -105.2705, label: 'Boulder' },
  'colorado-springs': { lat: 38.8339, lng: -104.8214, label: 'Colorado Springs' },
  'fort-collins': { lat: 40.5853, lng: -105.0844, label: 'Fort Collins' },
  'manitou-springs': { lat: 38.8586, lng: -104.9175, label: 'Manitou Springs' },
  aspen: { lat: 39.1911, lng: -106.8175, label: 'Aspen' },
  vail: { lat: 39.6403, lng: -106.3742, label: 'Vail' },
  breckenridge: { lat: 39.4817, lng: -106.0384, label: 'Breckenridge' },
  'steamboat-springs': { lat: 40.4850, lng: -106.8317, label: 'Steamboat Springs' },
  telluride: { lat: 37.9375, lng: -107.8123, label: 'Telluride' },
  'winter-park': { lat: 39.8917, lng: -105.7631, label: 'Winter Park' },
  'crested-butte': { lat: 38.8697, lng: -106.9878, label: 'Crested Butte' },
  keystone: { lat: 39.6069, lng: -105.9497, label: 'Keystone' },
  'estes-park': { lat: 40.3772, lng: -105.5217, label: 'Estes Park' },
  'great-sand-dunes': { lat: 37.7329, lng: -105.5121, label: 'Great Sand Dunes' },
  'mesa-verde': { lat: 37.1838, lng: -108.4887, label: 'Mesa Verde' },
  'black-canyon': { lat: 38.5754, lng: -107.7416, label: 'Black Canyon' },
  'glenwood-springs': { lat: 39.5505, lng: -107.3248, label: 'Glenwood Springs' },
  durango: { lat: 37.2753, lng: -107.8801, label: 'Durango' },
  ouray: { lat: 38.0228, lng: -107.6714, label: 'Ouray' },
};
